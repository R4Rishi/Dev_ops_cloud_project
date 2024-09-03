resource "aws_security_group" "allow_ssh" {
  name        = var.sg_name
  description = "Allow SSH inbound traffic"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Change as needed
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # All traffic
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = var.sg_name
  }
}

output "security_group_id" {
  value = aws_security_group.allow_ssh.id
}

# i am not providing any value in the code because this code is publically viewed.