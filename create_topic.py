import boto3 

name="Test topic"
endpoint="name@example.com"

sns_client = boto3.client('sns', verify=False)
topic = sns_client.create_topic(Name="Test")
#print("Created topic ARN ", topic['TopicArn'])

#subscription = sns_client.subscribe(TopicArn=topic['TopicArn'], Protocol="email", Endpoint=endpoint, ReturnSubscriptionArn=True)
#print("Subscribed ", subscribe_email, " to ", topic['topicArn'])


