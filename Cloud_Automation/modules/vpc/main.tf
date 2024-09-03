resource "aws_vpc" "main" {
  cidr_block = var.cidr_block
  enable_dns_support = true
  enable_dns_hostnames = true
  tags = {
    Name = var.vpc_name
  }
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24" # Change as needed
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1a" # Change as needed
  tags = {
    Name = "${var.vpc_name}-public-subnet"
  }
}

output "vpc_id" {
  value = aws_vpc.main.id
}

output "public_subnet_id" {
  value = aws_subnet.public.id
}


#I am not chnaging or providind sensitive information as it is publically avialable