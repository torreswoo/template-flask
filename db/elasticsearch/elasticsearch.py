# -*- coding: utf-8 -*-
import datetime

import pytest
from elasticsearch import Elasticsearch, helpers

elasticsearch_host = "http://test-elasticsearch-master.s2.krane.9rum.cc:9200"
client = Elasticsearch(hosts=elasticsearch_host)

KST = datetime.timezone(datetime.timedelta(hours=9))

def search_topic_offset(cluster, topic, partition=None):
    body = {
        'query': {
            'bool': {
                'must': [
                    {'match': {'cluster': cluster}},
                    {'match': {'topic': topic}},
                ],
                'filter': {'range': {'@timestamp': {'gt': 'now-30s'}}},
            },
        },
        'sort': [
            {'topic': {'order': 'desc'}},
            {'partition': {'order': 'asc'}}
        ],
        "size": 200,
        '_source': ['cluster', 'topic', 'partition', 'offset', '@timestamp'],
    }

    if partition:
        body['query']['bool']['must']['match'] = {'partition': partition}

    res = client.search(index='mobdata-kafka-topic-*',
                        body=body,
                        )

    return [x['_source'] for x in res['hits']['hits']]


@pytest.mark.skip(reason='pass')
def test_search_topic_offset():
    for x in search_topic_offset('dev-data', 'mobdata-ab-test-aggregation'):
        print(x)