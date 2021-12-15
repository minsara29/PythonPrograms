resource "local_file" "pet" {
  filename = var.filename
  #    content = var.content
  content = "my favorite pet is ${random_pet.mypet.id}" # depends random_pet resource output value

  #    depends_on = [
  #    "random_pet.mypet" #explicit dependency
  #    ]
}

resource "random_pet" "mypet" {
  prefix    = var.prefix
  separator = var.separator
  length    = var.length
}

# to store the value in output variable

output "rand_petname" {
  value       = random_pet.mypet.id
  description = "the id generated from resource random_pet"
}

#commands

# terraform validate
# terraform fmt
# terraform show
# terraform show -json
# terraform providers
# terraform providers mirror C:\\Users\\ktamilraj\\Documents\\GitHub\\PythonPrograms\\Terraform\\new_local_file
# terraform output
# terraform validate pet-name
# terraform refresh # update statefile if any manual intervention happened
# terraform graph # for graph viz # apt install graphviz -y
                  # terraform graph | dot -Tsvg > graph.svg

# life cycle rule
# dont delete before new resource create or keep older resource

#resource "local_file" "pet" {
#  filename = var.filename
#  #    content = var.content
#  content = "my favorite pet is ${random_pet.mypet.id}" # depends random_pet resource output value
#  file_permission = "0700"
#
#  #    depends_on = [
#  #    "random_pet.mypet" #explicit dependency
#  #    ]
#  lifecycle {
#    create_before_destroy = true
#    prevent_destroy = true
#  }
#}
