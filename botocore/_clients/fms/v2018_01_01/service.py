# THIS FILE IS AUTO-GENERATED. DO NOT EDIT THIS FILE BY HAND.

from botocore.client import BaseClient

class FMS(BaseClient):

    def associate_admin_account(self, **kwargs):
        """Sets the AWS Firewall Manager administrator account. AWS Firewall Manager must be associated with a master account in AWS Organizations or associated with a member account that has the appropriate permissions. If the account ID that you submit is not an AWS Organizations master account, AWS Firewall Manager will set the appropriate permissions for the given member account.
        
         
        
        The account that you associate with AWS Firewall Manager is called the AWS Firewall manager administrator account. 
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/AssociateAdminAccount>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.associate_admin_account(
              AdminAccount='string'
          )
        :type AdminAccount: string
        :param AdminAccount: **[REQUIRED]** 
        
          The AWS account ID to associate with AWS Firewall Manager as the AWS Firewall Manager administrator account. This can be an AWS Organizations master account or a member account. For more information about AWS Organizations and master accounts, see `Managing the AWS Accounts in Your Organization <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html>`__ .
        
          
        
        
        
        :returns: None
        """
        return self._make_api_call("AssociateAdminAccount", kwargs)

    def delete_notification_channel(self, **kwargs):
        """Deletes an AWS Firewall Manager association with the IAM role and the Amazon Simple Notification Service (SNS) topic that is used to record AWS Firewall Manager SNS logs.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/DeleteNotificationChannel>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.delete_notification_channel()
          
        
        :returns: None
        """
        return self._make_api_call("DeleteNotificationChannel", kwargs)

    def delete_policy(self, **kwargs):
        """Permanently deletes an AWS Firewall Manager policy. 
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/DeletePolicy>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.delete_policy(
              PolicyId='string'
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]** 
        
          The ID of the policy that you want to delete. ``PolicyId`` is returned by ``PutPolicy`` and by ``ListPolicies`` .
        
          
        
        
        
        :returns: None
        """
        return self._make_api_call("DeletePolicy", kwargs)

    def disassociate_admin_account(self, **kwargs):
        """Disassociates the account that has been set as the AWS Firewall Manager administrator account. You will need to submit an ``AssociateAdminAccount`` request to set a new account as the AWS Firewall administrator.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/DisassociateAdminAccount>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_admin_account()
          
        
        :returns: None
        """
        return self._make_api_call("DisassociateAdminAccount", kwargs)

    def get_admin_account(self, **kwargs):
        """Returns the AWS Organizations master account that is associated with AWS Firewall Manager as the AWS Firewall Manager administrator.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetAdminAccount>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.get_admin_account()
          
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {
                'AdminAccount': 'string'
            }
          **Response Structure** 
        
          
        
          - *(dict) --* 
            
        
            - **AdminAccount** *(string) --* 
        
              The AWS account that is set as the AWS Firewall Manager administrator.
        
              
        
        """
        return self._make_api_call("GetAdminAccount", kwargs)

    def get_compliance_detail(self, **kwargs):
        """Returns detailed compliance information about the specified member account. Details include resources that are in and out of compliance with the specified policy. Resources are considered non-compliant if the specified policy has not been applied to them.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetComplianceDetail>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.get_compliance_detail(
              PolicyId='string',
              MemberAccount='string'
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]** 
        
          The ID of the policy that you want to get the details for. ``PolicyId`` is returned by ``PutPolicy`` and by ``ListPolicies`` .
        
          
        
        
        :type MemberAccount: string
        :param MemberAccount: **[REQUIRED]** 
        
          The AWS account that owns the resources that you want to get the details for.
        
          
        
        
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {
                'PolicyComplianceDetail': {
                    'PolicyOwner': 'string',
                    'PolicyId': 'string',
                    'MemberAccount': 'string',
                    'Violators': [
                        {
                            'ResourceId': 'string',
                            'ViolationReason': 'WEB_ACL_MISSING_RULE_GROUP'|'RESOURCE_MISSING_WEB_ACL'|'RESOURCE_INCORRECT_WEB_ACL',
                            'ResourceType': 'string'
                        },
                    ],
                    'EvaluationLimitExceeded': True|False,
                    'ExpiredAt': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          
        
          - *(dict) --* 
            
        
            - **PolicyComplianceDetail** *(dict) --* 
        
              Information about the resources and the policy that you specified in the ``GetComplianceDetail`` request.
        
              
              
        
              - **PolicyOwner** *(string) --* 
        
                The AWS account that created the AWS Firewall Manager policy.
        
                
              
        
              - **PolicyId** *(string) --* 
        
                The ID of the AWS Firewall Manager policy.
        
                
              
        
              - **MemberAccount** *(string) --* 
        
                The AWS account ID.
        
                
              
        
              - **Violators** *(list) --* 
        
                An array of resources that are not protected by the policy.
        
                
                
        
                - *(dict) --* 
        
                  Details of the resource that is not protected by the policy.
        
                  
                  
        
                  - **ResourceId** *(string) --* 
        
                    The resource ID.
        
                    
                  
        
                  - **ViolationReason** *(string) --* 
        
                    The reason that the resource is not protected by the policy.
        
                    
                  
        
                  - **ResourceType** *(string) --* 
        
                    The resource type. This is in the format shown in `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ . Valid values are ``AWS::ElasticLoadBalancingV2::LoadBalancer`` or ``AWS::CloudFront::Distribution`` .
        
                    
              
            
              
        
              - **EvaluationLimitExceeded** *(boolean) --* 
        
                Indicates if over 100 resources are non-compliant with the AWS Firewall Manager policy.
        
                
              
        
              - **ExpiredAt** *(datetime) --* 
        
                A time stamp that indicates when the returned information should be considered out-of-date.
        
                
          
        
        """
        return self._make_api_call("GetComplianceDetail", kwargs)

    def get_notification_channel(self, **kwargs):
        """Returns information about the Amazon Simple Notification Service (SNS) topic that is used to record AWS Firewall Manager SNS logs.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetNotificationChannel>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.get_notification_channel()
          
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {
                'SnsTopicArn': 'string',
                'SnsRoleName': 'string'
            }
          **Response Structure** 
        
          
        
          - *(dict) --* 
            
        
            - **SnsTopicArn** *(string) --* 
        
              The SNS topic that records AWS Firewall Manager activity. 
        
              
            
        
            - **SnsRoleName** *(string) --* 
        
              The IAM role that is used by AWS Firewall Manager to record activity to SNS.
        
              
        
        """
        return self._make_api_call("GetNotificationChannel", kwargs)

    def get_policy(self, **kwargs):
        """Returns information about the specified AWS Firewall Manager policy.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetPolicy>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.get_policy(
              PolicyId='string'
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]** 
        
          The ID of the AWS Firewall Manager policy that you want the details for.
        
          
        
        
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {
                'Policy': {
                    'PolicyId': 'string',
                    'PolicyName': 'string',
                    'PolicyUpdateToken': 'string',
                    'SecurityServicePolicyData': {
                        'Type': 'WAF',
                        'ManagedServiceData': 'string'
                    },
                    'ResourceType': 'string',
                    'ResourceTags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'ExcludeResourceTags': True|False,
                    'RemediationEnabled': True|False
                },
                'PolicyArn': 'string'
            }
          **Response Structure** 
        
          
        
          - *(dict) --* 
            
        
            - **Policy** *(dict) --* 
        
              Information about the specified AWS Firewall Manager policy.
        
              
              
        
              - **PolicyId** *(string) --* 
        
                The ID of the AWS Firewall Manager policy.
        
                
              
        
              - **PolicyName** *(string) --* 
        
                The friendly name of the AWS Firewall Manager policy.
        
                
              
        
              - **PolicyUpdateToken** *(string) --* 
        
                A unique identifier for each update to the policy. When issuing a ``PutPolicy`` request, the ``PolicyUpdateToken`` in the request must match the ``PolicyUpdateToken`` of the current policy version. To get the ``PolicyUpdateToken`` of the current policy version, use a ``GetPolicy`` request.
        
                
              
        
              - **SecurityServicePolicyData** *(dict) --* 
        
                Details about the security service that is being used to protect the resources.
        
                
                
        
                - **Type** *(string) --* 
        
                  The service that the policy is using to protect the resources. This value is ``WAF`` .
        
                  
                
        
                - **ManagedServiceData** *(string) --* 
        
                  Details about the service. This contains ``WAF`` data in JSON format, as shown in the following example:
        
                   
        
                   ``ManagedServiceData": "{\"type\": \"WAF\", \"ruleGroups\": [{\"id\": \"12345678-1bcd-9012-efga-0987654321ab\", \"overrideAction\" : {\"type\": \"COUNT\"}}], \"defaultAction\": {\"type\": \"BLOCK\"}}``  
        
                  
            
              
        
              - **ResourceType** *(string) --* 
        
                The type of resource to protect with the policy, either an Application Load Balancer or a CloudFront distribution. This is in the format shown in `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ . Valid values are ``AWS::ElasticLoadBalancingV2::LoadBalancer`` or ``AWS::CloudFront::Distribution`` .
        
                
              
        
              - **ResourceTags** *(list) --* 
        
                An array of ``ResourceTag`` objects.
        
                
                
        
                - *(dict) --* 
        
                  The resource tags that AWS Firewall Manager uses to determine if a particular resource should be included or excluded from protection by the AWS Firewall Manager policy. Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. Tags are combined with an "OR." That is, if you add more than one tag, if any of the tags matches, the resource is considered a match for the include or exclude. `Working with Tag Editor <https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html>`__ .
        
                  
                  
        
                  - **Key** *(string) --* 
        
                    The resource tag key.
        
                    
                  
        
                  - **Value** *(string) --* 
        
                    The resource tag value.
        
                    
              
            
              
        
              - **ExcludeResourceTags** *(boolean) --* 
        
                If set to ``True`` , resources with the tags that are specified in the ``ResourceTag`` array are not protected by the policy. If set to ``False`` , and the ``ResourceTag`` array is not null, only resources with the specified tags are associated with the policy.
        
                
              
        
              - **RemediationEnabled** *(boolean) --* 
        
                Indicates if the policy should be automatically applied to new resources.
        
                
          
            
        
            - **PolicyArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the specified policy.
        
              
        
        """
        return self._make_api_call("GetPolicy", kwargs)

    def list_compliance_status(self, **kwargs):
        """Returns an array of ``PolicyComplianceStatus`` objects in the response. Use ``PolicyComplianceStatus`` to get a summary of which member accounts are protected by the specified policy. 
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/ListComplianceStatus>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.list_compliance_status(
              PolicyId='string',
              NextToken='string',
              MaxResults=123
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]** 
        
          The ID of the AWS Firewall Manager policy that you want the details for.
        
          
        
        
        :type NextToken: string
        :param NextToken: 
        
          If you specify a value for ``MaxResults`` and you have more ``PolicyComplianceStatus`` objects than the number that you specify for ``MaxResults`` , AWS Firewall Manager returns a ``NextToken`` value in the response that allows you to list another group of ``PolicyComplianceStatus`` objects. For the second and subsequent ``ListComplianceStatus`` requests, specify the value of ``NextToken`` from the previous response to get information about another batch of ``PolicyComplianceStatus`` objects.
        
          
        
        
        :type MaxResults: integer
        :param MaxResults: 
        
          Specifies the number of ``PolicyComplianceStatus`` objects that you want AWS Firewall Manager to return for this request. If you have more ``PolicyComplianceStatus`` objects than the number that you specify for ``MaxResults`` , the response includes a ``NextToken`` value that you can use to get another batch of ``PolicyComplianceStatus`` objects.
        
          
        
        
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {
                'PolicyComplianceStatusList': [
                    {
                        'PolicyOwner': 'string',
                        'PolicyId': 'string',
                        'PolicyName': 'string',
                        'MemberAccount': 'string',
                        'EvaluationResults': [
                            {
                                'ComplianceStatus': 'COMPLIANT'|'NON_COMPLIANT',
                                'ViolatorCount': 123,
                                'EvaluationLimitExceeded': True|False
                            },
                        ],
                        'LastUpdated': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure** 
        
          
        
          - *(dict) --* 
            
        
            - **PolicyComplianceStatusList** *(list) --* 
        
              An array of ``PolicyComplianceStatus`` objects.
        
              
              
        
              - *(dict) --* 
        
                Indicates whether the account is compliant with the specified policy. An account is considered non-compliant if it includes resources that are not protected by the policy.
        
                
                
        
                - **PolicyOwner** *(string) --* 
        
                  The AWS account that created the AWS Firewall Manager policy.
        
                  
                
        
                - **PolicyId** *(string) --* 
        
                  The ID of the AWS Firewall Manager policy.
        
                  
                
        
                - **PolicyName** *(string) --* 
        
                  The friendly name of the AWS Firewall Manager policy.
        
                  
                
        
                - **MemberAccount** *(string) --* 
        
                  The member account ID.
        
                  
                
        
                - **EvaluationResults** *(list) --* 
        
                  An array of ``EvaluationResult`` objects.
        
                  
                  
        
                  - *(dict) --* 
        
                    Describes the compliance status for the account. An account is considered non-compliant if it includes resources that are not protected by the specified policy.
        
                    
                    
        
                    - **ComplianceStatus** *(string) --* 
        
                      Describes an AWS account's compliance with the AWS Firewall Manager policy.
        
                      
                    
        
                    - **ViolatorCount** *(integer) --* 
        
                      Number of resources that are non-compliant with the specified policy. A resource is considered non-compliant if it is not associated with the specified policy.
        
                      
                    
        
                    - **EvaluationLimitExceeded** *(boolean) --* 
        
                      Indicates that over 100 resources are non-compliant with the AWS Firewall Manager policy.
        
                      
                
              
                
        
                - **LastUpdated** *(datetime) --* 
        
                  Time stamp of the last update to the ``EvaluationResult`` objects.
        
                  
            
          
            
        
            - **NextToken** *(string) --* 
        
              If you have more ``PolicyComplianceStatus`` objects than the number that you specified for ``MaxResults`` in the request, the response includes a ``NextToken`` value. To list more ``PolicyComplianceStatus`` objects, submit another ``ListComplianceStatus`` request, and specify the ``NextToken`` value from the response in the ``NextToken`` value in the next request.
        
              
        
        """
        return self._make_api_call("ListComplianceStatus", kwargs)

    def list_policies(self, **kwargs):
        """Returns an array of ``PolicySummary`` objects in the response.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/ListPolicies>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.list_policies(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken: 
        
          If you specify a value for ``MaxResults`` and you have more ``PolicySummary`` objects than the number that you specify for ``MaxResults`` , AWS Firewall Manager returns a ``NextToken`` value in the response that allows you to list another group of ``PolicySummary`` objects. For the second and subsequent ``ListPolicies`` requests, specify the value of ``NextToken`` from the previous response to get information about another batch of ``PolicySummary`` objects.
        
          
        
        
        :type MaxResults: integer
        :param MaxResults: 
        
          Specifies the number of ``PolicySummary`` objects that you want AWS Firewall Manager to return for this request. If you have more ``PolicySummary`` objects than the number that you specify for ``MaxResults`` , the response includes a ``NextToken`` value that you can use to get another batch of ``PolicySummary`` objects.
        
          
        
        
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {
                'PolicyList': [
                    {
                        'PolicyArn': 'string',
                        'PolicyId': 'string',
                        'PolicyName': 'string',
                        'ResourceType': 'string',
                        'SecurityServiceType': 'WAF',
                        'RemediationEnabled': True|False
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure** 
        
          
        
          - *(dict) --* 
            
        
            - **PolicyList** *(list) --* 
        
              An array of ``PolicySummary`` objects.
        
              
              
        
              - *(dict) --* 
        
                Details of the AWS Firewall Manager policy. 
        
                
                
        
                - **PolicyArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the specified policy.
        
                  
                
        
                - **PolicyId** *(string) --* 
        
                  The ID of the specified policy.
        
                  
                
        
                - **PolicyName** *(string) --* 
        
                  The friendly name of the specified policy.
        
                  
                
        
                - **ResourceType** *(string) --* 
        
                  The type of resource to protect with the policy, either an Application Load Balancer or a CloudFront distribution. This is in the format shown in `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ . Valid values are ``AWS::ElasticLoadBalancingV2::LoadBalancer`` or ``AWS::CloudFront::Distribution`` .
        
                  
                
        
                - **SecurityServiceType** *(string) --* 
        
                  The service that the policy is using to protect the resources. This value is ``WAF`` .
        
                  
                
        
                - **RemediationEnabled** *(boolean) --* 
        
                  Indicates if the policy should be automatically applied to new resources.
        
                  
            
          
            
        
            - **NextToken** *(string) --* 
        
              If you have more ``PolicySummary`` objects than the number that you specified for ``MaxResults`` in the request, the response includes a ``NextToken`` value. To list more ``PolicySummary`` objects, submit another ``ListPolicies`` request, and specify the ``NextToken`` value from the response in the ``NextToken`` value in the next request.
        
              
        
        """
        return self._make_api_call("ListPolicies", kwargs)

    def put_notification_channel(self, **kwargs):
        """Designates the IAM role and Amazon Simple Notification Service (SNS) topic that AWS Firewall Manager uses to record SNS logs.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/PutNotificationChannel>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.put_notification_channel(
              SnsTopicArn='string',
              SnsRoleName='string'
          )
        :type SnsTopicArn: string
        :param SnsTopicArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the SNS topic that collects notifications from AWS Firewall Manager.
        
          
        
        
        :type SnsRoleName: string
        :param SnsRoleName: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to record AWS Firewall Manager activity. 
        
          
        
        
        
        :returns: None
        """
        return self._make_api_call("PutNotificationChannel", kwargs)

    def put_policy(self, **kwargs):
        """Creates an AWS Firewall Manager policy.
        
        
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/PutPolicy>`_
        
        
        **Request Syntax** 
        ::
        
          response = client.put_policy(
              Policy={
                  'PolicyId': 'string',
                  'PolicyName': 'string',
                  'PolicyUpdateToken': 'string',
                  'SecurityServicePolicyData': {
                      'Type': 'WAF',
                      'ManagedServiceData': 'string'
                  },
                  'ResourceType': 'string',
                  'ResourceTags': [
                      {
                          'Key': 'string',
                          'Value': 'string'
                      },
                  ],
                  'ExcludeResourceTags': True|False,
                  'RemediationEnabled': True|False
              }
          )
        :type Policy: dict
        :param Policy: **[REQUIRED]** 
        
          The details of the AWS Firewall Manager policy to be created.
        
          
        
        
          - **PolicyId** *(string) --* 
        
            The ID of the AWS Firewall Manager policy.
        
            
        
          
          - **PolicyName** *(string) --* **[REQUIRED]** 
        
            The friendly name of the AWS Firewall Manager policy.
        
            
        
          
          - **PolicyUpdateToken** *(string) --* 
        
            A unique identifier for each update to the policy. When issuing a ``PutPolicy`` request, the ``PolicyUpdateToken`` in the request must match the ``PolicyUpdateToken`` of the current policy version. To get the ``PolicyUpdateToken`` of the current policy version, use a ``GetPolicy`` request.
        
            
        
          
          - **SecurityServicePolicyData** *(dict) --* **[REQUIRED]** 
        
            Details about the security service that is being used to protect the resources.
        
            
        
          
            - **Type** *(string) --* **[REQUIRED]** 
        
              The service that the policy is using to protect the resources. This value is ``WAF`` .
        
              
        
            
            - **ManagedServiceData** *(string) --* 
        
              Details about the service. This contains ``WAF`` data in JSON format, as shown in the following example:
        
               
        
               ``ManagedServiceData": "{\"type\": \"WAF\", \"ruleGroups\": [{\"id\": \"12345678-1bcd-9012-efga-0987654321ab\", \"overrideAction\" : {\"type\": \"COUNT\"}}], \"defaultAction\": {\"type\": \"BLOCK\"}}``  
        
              
        
            
          
          - **ResourceType** *(string) --* **[REQUIRED]** 
        
            The type of resource to protect with the policy, either an Application Load Balancer or a CloudFront distribution. This is in the format shown in `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ . Valid values are ``AWS::ElasticLoadBalancingV2::LoadBalancer`` or ``AWS::CloudFront::Distribution`` .
        
            
        
          
          - **ResourceTags** *(list) --* 
        
            An array of ``ResourceTag`` objects.
        
            
        
          
            - *(dict) --* 
        
              The resource tags that AWS Firewall Manager uses to determine if a particular resource should be included or excluded from protection by the AWS Firewall Manager policy. Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. Tags are combined with an "OR." That is, if you add more than one tag, if any of the tags matches, the resource is considered a match for the include or exclude. `Working with Tag Editor <https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html>`__ .
        
              
        
            
              - **Key** *(string) --* **[REQUIRED]** 
        
                The resource tag key.
        
                
        
              
              - **Value** *(string) --* 
        
                The resource tag value.
        
                
        
              
            
        
          - **ExcludeResourceTags** *(boolean) --* **[REQUIRED]** 
        
            If set to ``True`` , resources with the tags that are specified in the ``ResourceTag`` array are not protected by the policy. If set to ``False`` , and the ``ResourceTag`` array is not null, only resources with the specified tags are associated with the policy.
        
            
        
          
          - **RemediationEnabled** *(boolean) --* **[REQUIRED]** 
        
            Indicates if the policy should be automatically applied to new resources.
        
            
        
          
        
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          
          ::
        
            {
                'Policy': {
                    'PolicyId': 'string',
                    'PolicyName': 'string',
                    'PolicyUpdateToken': 'string',
                    'SecurityServicePolicyData': {
                        'Type': 'WAF',
                        'ManagedServiceData': 'string'
                    },
                    'ResourceType': 'string',
                    'ResourceTags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'ExcludeResourceTags': True|False,
                    'RemediationEnabled': True|False
                },
                'PolicyArn': 'string'
            }
          **Response Structure** 
        
          
        
          - *(dict) --* 
            
        
            - **Policy** *(dict) --* 
        
              The details of the AWS Firewall Manager policy that was created.
        
              
              
        
              - **PolicyId** *(string) --* 
        
                The ID of the AWS Firewall Manager policy.
        
                
              
        
              - **PolicyName** *(string) --* 
        
                The friendly name of the AWS Firewall Manager policy.
        
                
              
        
              - **PolicyUpdateToken** *(string) --* 
        
                A unique identifier for each update to the policy. When issuing a ``PutPolicy`` request, the ``PolicyUpdateToken`` in the request must match the ``PolicyUpdateToken`` of the current policy version. To get the ``PolicyUpdateToken`` of the current policy version, use a ``GetPolicy`` request.
        
                
              
        
              - **SecurityServicePolicyData** *(dict) --* 
        
                Details about the security service that is being used to protect the resources.
        
                
                
        
                - **Type** *(string) --* 
        
                  The service that the policy is using to protect the resources. This value is ``WAF`` .
        
                  
                
        
                - **ManagedServiceData** *(string) --* 
        
                  Details about the service. This contains ``WAF`` data in JSON format, as shown in the following example:
        
                   
        
                   ``ManagedServiceData": "{\"type\": \"WAF\", \"ruleGroups\": [{\"id\": \"12345678-1bcd-9012-efga-0987654321ab\", \"overrideAction\" : {\"type\": \"COUNT\"}}], \"defaultAction\": {\"type\": \"BLOCK\"}}``  
        
                  
            
              
        
              - **ResourceType** *(string) --* 
        
                The type of resource to protect with the policy, either an Application Load Balancer or a CloudFront distribution. This is in the format shown in `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ . Valid values are ``AWS::ElasticLoadBalancingV2::LoadBalancer`` or ``AWS::CloudFront::Distribution`` .
        
                
              
        
              - **ResourceTags** *(list) --* 
        
                An array of ``ResourceTag`` objects.
        
                
                
        
                - *(dict) --* 
        
                  The resource tags that AWS Firewall Manager uses to determine if a particular resource should be included or excluded from protection by the AWS Firewall Manager policy. Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. Tags are combined with an "OR." That is, if you add more than one tag, if any of the tags matches, the resource is considered a match for the include or exclude. `Working with Tag Editor <https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html>`__ .
        
                  
                  
        
                  - **Key** *(string) --* 
        
                    The resource tag key.
        
                    
                  
        
                  - **Value** *(string) --* 
        
                    The resource tag value.
        
                    
              
            
              
        
              - **ExcludeResourceTags** *(boolean) --* 
        
                If set to ``True`` , resources with the tags that are specified in the ``ResourceTag`` array are not protected by the policy. If set to ``False`` , and the ``ResourceTag`` array is not null, only resources with the specified tags are associated with the policy.
        
                
              
        
              - **RemediationEnabled** *(boolean) --* 
        
                Indicates if the policy should be automatically applied to new resources.
        
                
          
            
        
            - **PolicyArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the policy that was created.
        
              
        
        """
        return self._make_api_call("PutPolicy", kwargs)
