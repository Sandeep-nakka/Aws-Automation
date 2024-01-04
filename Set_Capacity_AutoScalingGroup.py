import boto3


class AutoScalingGroup:
    asg_client = boto3.client('autoscaling', region_name='us-east-1')

    def set_asg(self, Asgname, Minimumsize, Desiredsize):
        response = self.asg_client.update_auto_scaling_group(
            AutoScalingGroupName=Asgname,
            MinSize=Minimumsize,
            DesiredCapacity=Desiredsize
        )
        print(f"Response: {response}")
        print(
            f"Updated Autoscaling group Successfully: {Asgname}: Minimum Size: {Minimumsize} : Desired Capacity: {Desiredsize}")

    response = asg_client.describe_auto_scaling_groups()
    Required_groups = response['AutoScalingGroups']
    print(f"AutoScaling Groups: {Required_groups}")
    for group in Required_groups:
        auto_scaling_group_name = group['AutoScalingGroupName']
        set_asg(auto_scaling_group_name, 1, 1)


if __name__ == '__main__':
    AutoScalingGroup()
