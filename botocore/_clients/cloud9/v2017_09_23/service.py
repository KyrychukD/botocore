# THIS FILE IS AUTO-GENERATED. DO NOT EDIT THIS FILE BY HAND.

from botocore.client import BaseClient

class Cloud9(BaseClient):

    def create_environment_ec2(self, **kwargs):
        """Creates an AWS Cloud9 development environment, launches an Amazon Elastic Compute Cloud (Amazon EC2) instance, and then connects from the instance to the environment.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloud9-2017-09-23/CreateEnvironmentEC2>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.create_environment_ec2(
              name='string',
              description='string',
              clientRequestToken='string',
              instanceType='string',
              subnetId='string',
              automaticStopTimeMinutes=123,
              ownerArn='string'
          )
        :type name: string
        :param name: **[REQUIRED]** 
        
          The name of the environment to create.
        
           
        
          This name is visible to other AWS IAM users in the same AWS account.
        
          
        
        
        :type description: string
        :param description: 
        
          The description of the environment to create.
        
          
        
        
        :type clientRequestToken: string
        :param clientRequestToken: 
        
          A unique, case-sensitive string that helps AWS Cloud9 to ensure this operation completes no more than one time.
        
           
        
          For more information, see `Client Tokens <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html>`__ in the *Amazon EC2 API Reference* .
        
          
        
        
        :type instanceType: string
        :param instanceType: **[REQUIRED]** 
        
          The type of instance to connect to the environment (for example, ``t2.micro`` ).
        
          
        
        
        :type subnetId: string
        :param subnetId: 
        
          The ID of the subnet in Amazon VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance.
        
          
        
        
        :type automaticStopTimeMinutes: integer
        :param automaticStopTimeMinutes: 
        
          The number of minutes until the running instance is shut down after the environment has last been used.
        
          
        
        
        :type ownerArn: string
        :param ownerArn: 
        
          The Amazon Resource Name (ARN) of the environment owner. This ARN can be the ARN of any AWS IAM principal. If this value is not specified, the ARN defaults to this environment's creator.
        
          
        
        
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {
                'environmentId': 'string'
            }
          **Response Structure** 
        
          
        
          - *(dict) --* 
            
        
            - **environmentId** *(string) --* 
        
              The ID of the environment that was created.
        
              
        
        """
        return self._make_api_call("CreateEnvironmentEC2", kwargs)

    def create_environment_membership(self, **kwargs):
        """Adds an environment member to an AWS Cloud9 development environment.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloud9-2017-09-23/CreateEnvironmentMembership>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.create_environment_membership(
              environmentId='string',
              userArn='string',
              permissions='read-write'|'read-only'
          )
        :type environmentId: string
        :param environmentId: **[REQUIRED]** 
        
          The ID of the environment that contains the environment member you want to add.
        
          
        
        
        :type userArn: string
        :param userArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the environment member you want to add.
        
          
        
        
        :type permissions: string
        :param permissions: **[REQUIRED]** 
        
          The type of environment member permissions you want to associate with this environment member. Available values include:
        
           
        
           
          * ``read-only`` : Has read-only access to the environment. 
           
          * ``read-write`` : Has read-write access to the environment. 
           
        
          
        
        
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {
                'membership': {
                    'permissions': 'owner'|'read-write'|'read-only',
                    'userId': 'string',
                    'userArn': 'string',
                    'environmentId': 'string',
                    'lastAccess': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          
        
          - *(dict) --* 
            
        
            - **membership** *(dict) --* 
        
              Information about the environment member that was added.
        
              
              
        
              - **permissions** *(string) --* 
        
                The type of environment member permissions associated with this environment member. Available values include:
        
                 
        
                 
                * ``owner`` : Owns the environment. 
                 
                * ``read-only`` : Has read-only access to the environment. 
                 
                * ``read-write`` : Has read-write access to the environment. 
                 
        
                
              
        
              - **userId** *(string) --* 
        
                The user ID in AWS Identity and Access Management (AWS IAM) of the environment member.
        
                
              
        
              - **userArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the environment member.
        
                
              
        
              - **environmentId** *(string) --* 
        
                The ID of the environment for the environment member.
        
                
              
        
              - **lastAccess** *(datetime) --* 
        
                The time, expressed in epoch time format, when the environment member last opened the environment.
        
                
          
        
        """
        return self._make_api_call("CreateEnvironmentMembership", kwargs)

    def delete_environment(self, **kwargs):
        """Deletes an AWS Cloud9 development environment. If an Amazon EC2 instance is connected to the environment, also terminates the instance.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloud9-2017-09-23/DeleteEnvironment>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.delete_environment(
              environmentId='string'
          )
        :type environmentId: string
        :param environmentId: **[REQUIRED]** 
        
          The ID of the environment to delete.
        
          
        
        
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {}
          **Response Structure** 
        
          
        
          - *(dict) --* 
        
        """
        return self._make_api_call("DeleteEnvironment", kwargs)

    def delete_environment_membership(self, **kwargs):
        """Deletes an environment member from an AWS Cloud9 development environment.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloud9-2017-09-23/DeleteEnvironmentMembership>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.delete_environment_membership(
              environmentId='string',
              userArn='string'
          )
        :type environmentId: string
        :param environmentId: **[REQUIRED]** 
        
          The ID of the environment to delete the environment member from.
        
          
        
        
        :type userArn: string
        :param userArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the environment member to delete from the environment.
        
          
        
        
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {}
          **Response Structure** 
        
          
        
          - *(dict) --* 
        
        """
        return self._make_api_call("DeleteEnvironmentMembership", kwargs)

    def describe_environment_memberships(self, **kwargs):
        """Gets information about environment members for an AWS Cloud9 development environment.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloud9-2017-09-23/DescribeEnvironmentMemberships>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.describe_environment_memberships(
              userArn='string',
              environmentId='string',
              permissions=[
                  'owner'|'read-write'|'read-only',
              ],
              nextToken='string',
              maxResults=123
          )
        :type userArn: string
        :param userArn: 
        
          The Amazon Resource Name (ARN) of an individual environment member to get information about. If no value is specified, information about all environment members are returned.
        
          
        
        
        :type environmentId: string
        :param environmentId: 
        
          The ID of the environment to get environment member information about.
        
          
        
        
        :type permissions: list
        :param permissions: 
        
          The type of environment member permissions to get information about. Available values include:
        
           
        
           
          * ``owner`` : Owns the environment. 
           
          * ``read-only`` : Has read-only access to the environment. 
           
          * ``read-write`` : Has read-write access to the environment. 
           
        
           
        
          If no value is specified, information about all environment members are returned.
        
          
        
        
          - *(string) --* 
        
          
        
        :type nextToken: string
        :param nextToken: 
        
          During a previous call, if there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a *next token* . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.
        
          
        
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of environment members to get information about.
        
          
        
        
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {
                'memberships': [
                    {
                        'permissions': 'owner'|'read-write'|'read-only',
                        'userId': 'string',
                        'userArn': 'string',
                        'environmentId': 'string',
                        'lastAccess': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure** 
        
          
        
          - *(dict) --* 
            
        
            - **memberships** *(list) --* 
        
              Information about the environment members for the environment.
        
              
              
        
              - *(dict) --* 
        
                Information about an environment member for an AWS Cloud9 development environment.
        
                
                
        
                - **permissions** *(string) --* 
        
                  The type of environment member permissions associated with this environment member. Available values include:
        
                   
        
                   
                  * ``owner`` : Owns the environment. 
                   
                  * ``read-only`` : Has read-only access to the environment. 
                   
                  * ``read-write`` : Has read-write access to the environment. 
                   
        
                  
                
        
                - **userId** *(string) --* 
        
                  The user ID in AWS Identity and Access Management (AWS IAM) of the environment member.
        
                  
                
        
                - **userArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the environment member.
        
                  
                
        
                - **environmentId** *(string) --* 
        
                  The ID of the environment for the environment member.
        
                  
                
        
                - **lastAccess** *(datetime) --* 
        
                  The time, expressed in epoch time format, when the environment member last opened the environment.
        
                  
            
          
            
        
            - **nextToken** *(string) --* 
        
              If there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a *next token* . To get the next batch of items in the list, call this operation again, adding the next token to the call.
        
              
        
        """
        return self._make_api_call("DescribeEnvironmentMemberships", kwargs)

    def describe_environment_status(self, **kwargs):
        """Gets status information for an AWS Cloud9 development environment.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloud9-2017-09-23/DescribeEnvironmentStatus>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.describe_environment_status(
              environmentId='string'
          )
        :type environmentId: string
        :param environmentId: **[REQUIRED]** 
        
          The ID of the environment to get status information about.
        
          
        
        
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {
                'status': 'error'|'creating'|'connecting'|'ready'|'stopping'|'stopped'|'deleting',
                'message': 'string'
            }
          **Response Structure** 
        
          
        
          - *(dict) --* 
            
        
            - **status** *(string) --* 
        
              The status of the environment. Available values include:
        
               
        
               
              * ``connecting`` : The environment is connecting. 
               
              * ``creating`` : The environment is being created. 
               
              * ``deleting`` : The environment is being deleted. 
               
              * ``error`` : The environment is in an error state. 
               
              * ``ready`` : The environment is ready. 
               
              * ``stopped`` : The environment is stopped. 
               
              * ``stopping`` : The environment is stopping. 
               
        
              
            
        
            - **message** *(string) --* 
        
              Any informational message about the status of the environment.
        
              
        
        """
        return self._make_api_call("DescribeEnvironmentStatus", kwargs)

    def describe_environments(self, **kwargs):
        """Gets information about AWS Cloud9 development environments.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloud9-2017-09-23/DescribeEnvironments>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.describe_environments(
              environmentIds=[
                  'string',
              ]
          )
        :type environmentIds: list
        :param environmentIds: **[REQUIRED]** 
        
          The IDs of individual environments to get information about.
        
          
        
        
          - *(string) --* 
        
          
        
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {
                'environments': [
                    {
                        'id': 'string',
                        'name': 'string',
                        'description': 'string',
                        'type': 'ssh'|'ec2',
                        'arn': 'string',
                        'ownerArn': 'string'
                    },
                ]
            }
          **Response Structure** 
        
          
        
          - *(dict) --* 
            
        
            - **environments** *(list) --* 
        
              Information about the environments that are returned.
        
              
              
        
              - *(dict) --* 
        
                Information about an AWS Cloud9 development environment.
        
                
                
        
                - **id** *(string) --* 
        
                  The ID of the environment.
        
                  
                
        
                - **name** *(string) --* 
        
                  The name of the environment.
        
                  
                
        
                - **description** *(string) --* 
        
                  The description for the environment.
        
                  
                
        
                - **type** *(string) --* 
        
                  The type of environment. Valid values include the following:
        
                   
        
                   
                  * ``ec2`` : An Amazon Elastic Compute Cloud (Amazon EC2) instance connects to the environment. 
                   
                  * ``ssh`` : Your own server connects to the environment. 
                   
        
                  
                
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the environment.
        
                  
                
        
                - **ownerArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the environment owner.
        
                  
            
          
        
        """
        return self._make_api_call("DescribeEnvironments", kwargs)

    def list_environments(self, **kwargs):
        """Gets a list of AWS Cloud9 development environment identifiers.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloud9-2017-09-23/ListEnvironments>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.list_environments(
              nextToken='string',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken: 
        
          During a previous call, if there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a *next token* . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.
        
          
        
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of environments to get identifiers for.
        
          
        
        
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {
                'nextToken': 'string',
                'environmentIds': [
                    'string',
                ]
            }
          **Response Structure** 
        
          
        
          - *(dict) --* 
            
        
            - **nextToken** *(string) --* 
        
              If there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a *next token* . To get the next batch of items in the list, call this operation again, adding the next token to the call.
        
              
            
        
            - **environmentIds** *(list) --* 
        
              The list of environment identifiers.
        
              
              
        
              - *(string) --* 
          
        
        """
        return self._make_api_call("ListEnvironments", kwargs)

    def update_environment(self, **kwargs):
        """Changes the settings of an existing AWS Cloud9 development environment.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloud9-2017-09-23/UpdateEnvironment>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.update_environment(
              environmentId='string',
              name='string',
              description='string'
          )
        :type environmentId: string
        :param environmentId: **[REQUIRED]** 
        
          The ID of the environment to change settings.
        
          
        
        
        :type name: string
        :param name: 
        
          A replacement name for the environment.
        
          
        
        
        :type description: string
        :param description: 
        
          Any new or replacement description for the environment.
        
          
        
        
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {}
          **Response Structure** 
        
          
        
          - *(dict) --* 
        
        """
        return self._make_api_call("UpdateEnvironment", kwargs)

    def update_environment_membership(self, **kwargs):
        """Changes the settings of an existing environment member for an AWS Cloud9 development environment.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloud9-2017-09-23/UpdateEnvironmentMembership>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.update_environment_membership(
              environmentId='string',
              userArn='string',
              permissions='read-write'|'read-only'
          )
        :type environmentId: string
        :param environmentId: **[REQUIRED]** 
        
          The ID of the environment for the environment member whose settings you want to change.
        
          
        
        
        :type userArn: string
        :param userArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the environment member whose settings you want to change.
        
          
        
        
        :type permissions: string
        :param permissions: **[REQUIRED]** 
        
          The replacement type of environment member permissions you want to associate with this environment member. Available values include:
        
           
        
           
          * ``read-only`` : Has read-only access to the environment. 
           
          * ``read-write`` : Has read-write access to the environment. 
           
        
          
        
        
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {
                'membership': {
                    'permissions': 'owner'|'read-write'|'read-only',
                    'userId': 'string',
                    'userArn': 'string',
                    'environmentId': 'string',
                    'lastAccess': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          
        
          - *(dict) --* 
            
        
            - **membership** *(dict) --* 
        
              Information about the environment member whose settings were changed.
        
              
              
        
              - **permissions** *(string) --* 
        
                The type of environment member permissions associated with this environment member. Available values include:
        
                 
        
                 
                * ``owner`` : Owns the environment. 
                 
                * ``read-only`` : Has read-only access to the environment. 
                 
                * ``read-write`` : Has read-write access to the environment. 
                 
        
                
              
        
              - **userId** *(string) --* 
        
                The user ID in AWS Identity and Access Management (AWS IAM) of the environment member.
        
                
              
        
              - **userArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the environment member.
        
                
              
        
              - **environmentId** *(string) --* 
        
                The ID of the environment for the environment member.
        
                
              
        
              - **lastAccess** *(datetime) --* 
        
                The time, expressed in epoch time format, when the environment member last opened the environment.
        
                
          
        
        """
        return self._make_api_call("UpdateEnvironmentMembership", kwargs)
