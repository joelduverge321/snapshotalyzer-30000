import boto3

if __name__ == '__main__':
    session = boto3.Session(profile_name='shotty')

    ec2 = session.resource('ec2')

    #make sure the use has 'ec2Fullaccess' permission in IAM
    for i in ec2.instances.all():
        print(i)