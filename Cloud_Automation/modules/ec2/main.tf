resource "aws_instance" "web" {
  ami             = var.ami
  instance_type   = var.instance_type
  subnet_id       = var.subnet_id
  vpc_security_group_ids = [var.security_group_id]

  tags = {
    Name = "WebInstance"
  }
}

output "instance_id" {
  value = aws_instance.web.id
}

# I am not providing any values because it is publically viewed.