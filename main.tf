# Use the local provider
terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5.1"
    }
  }
}

# Create a local file
resource "local_file" "example" {
  filename = "${path.module}/output.txt"
  content  = "Hello from Terraform!"
}
