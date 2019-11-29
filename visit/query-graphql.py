#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
from urllib.parse import urlencode

#⊕ [webob-graphql/test_graphql.py at master · graphql-python/webob-graphql](https://github.com/graphql-python/webob-graphql/blob/master/tests/test_graphql.py)

print(urlencode(dict(query='{test}')))
print(urlencode(dict(query='{findAllBooks{id title}}')))
