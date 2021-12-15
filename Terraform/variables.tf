variable "filename" {
  default     = "C:\\Users\\ktamilraj\\Documents\\GitHub\\PythonPrograms\\Terraform\\pets.txt"
  type        = string
  description = "local file creation and location"
}

variable "content" {
  default     = "we love pets!"
  type        = string
  description = "content of the file"
}

variable "prefix" {
  default     = "Mrs"
  type        = string
  description = "prefix value for pets name"
}

variable "separator" {
  default     = "."
  type        = string
  description = "to merge the prefix with pet name"
}

variable "length" {
  default     = 1
  type        = number
  description = "length of the pets"
}

variable "list" {
  default     = ["mr", "mrs"] #var.list[0]
  type        = list(any)
  description = "length of the pets"
}

variable "map" {
  type = map(any)
  default = { "statement1" = "statement1" #var.map["statement1"]
    "statement2" = "statement2"
  }
  description = "length of the pets"
}

variable "set" {
  default     = ["mr", "mrs"] #var.list[0] # duplicate not allowed
  type        = set(string)
  description = "length of the pets"
}

variable "custom" {
  type = object({
    name         = string
    color        = string
    age          = number
    food         = list(string)
    favorite_pet = bool
  })
  default = {
    name         = "cat"
    color        = "black"
    age          = "3"
    food         = ["fish", "milk"]
    favorite_pet = true
  }
  description = "cats object type "
}

variable "tuple" {
  type        = tuple([string, number, bool])
  default     = ["cat", 1, true]
  description = "multiple data type"
}

# console display
#terraform output
#terraform output rand_petname
