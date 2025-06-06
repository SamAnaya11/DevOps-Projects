resource "aws_instance" "dove" {
  ami                    = data.aws_ami.ami_ID.id
  instance_type          = "t3.micro"
  key_name               = aws_key_pair.dovekey.key_name
  vpc_security_group_ids = [aws_security_group.dove-sg.id]
  availability_zone      = "us-east-1a"

  tags = {
    Name    = "Dove-web"
    Project = "Dove"
  }
}
output "instance_id" {
  value = aws_instance.dove.id
}


resource "aws_ec2_instance_state" "web-state" {
  instance_id = aws_instance.dove.id
  state       = "running"
}