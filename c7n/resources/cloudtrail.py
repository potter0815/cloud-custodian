# Copyright 2017 Capital One Services, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from c7n.manager import resources
from c7n.query import QueryResourceManager


@resources.register('cloudtrail')
class CloudTrail(QueryResourceManager):

    class resource_type(object):
        service = 'cloudtrail'
        enum_spec = ('describe_trails', 'trailList', None)
        #
        #detail_spec = (
        #    'get_event_selectors', 'TrailName', 'TrailArn', None)
        filter_name = 'trailNameList'
        filter_type = 'list'
        id = 'TrailArn'
        name = 'Name'
        dimension = None
        config_type = "AWS::CloudTrail::Trail"
