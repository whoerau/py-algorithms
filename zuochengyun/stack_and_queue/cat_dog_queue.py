class Pet():
    def __init__(self, _type: str, _name: str):
        self.type = _type  # cat or dog
        self.name = _name


class PetNode():
    def __init__(self, pet: Pet, count: int):
        self.pet = pet
        self.count = count


class CatDogQueue():
    def __init__(self):
        self.cat_queue = []
        self.dog_queue = []
        self.count = 0

    def add(self, pet: Pet):
        if pet.type == "cat":
            self.count += 1
            self.cat_queue.append(PetNode(pet, self.count))
        elif pet.type == "dog":
            self.count += 1
            self.dog_queue.append(PetNode(pet, self.count))
        else:
            raise Exception("type error")

    def poll_all(self) -> Pet:
        if self.cat_queue and self.dog_queue:
            if self.cat_queue[0].count < self.dog_queue[0].count:
                return self.cat_queue.pop(0)
            else:
                return self.dog_queue.pop(0)
        elif self.cat_queue:
            return self.cat_queue.pop(0)
        elif self.dog_queue:
            return self.dog_queue.pop(0)
        else:
            raise Exception("queue None")

    def poll_cat(self) -> Pet:
        if self.cat_queue:
            return self.cat_queue.pop(0)
        else:
            raise Exception("cat queue None")

    def poll_dog(self) -> Pet:
        if self.dog_queue:
            return self.dog_queue.pop(0)
        else:
            raise Exception("dog queue None")

    def is_empty(self):
        return self.cat_queue and self.dog_queue

    def is_cat_empty(self):
        return self.cat_queue

    def is_dog_empty(self):
        return self.dog_queue


if __name__ == '__main__':
    cgq = CatDogQueue()
    cgq.add(Pet("cat", "a"))
    cgq.add(Pet("dog", "g"))
    cgq.add(Pet("cat", "d"))
    cgq.add(Pet("dog", "f"))
    cgq.add(Pet("cat", "c"))
    cgq.add(Pet("dog", "v"))
    cgq.add(Pet("cat", "b"))
    cgq.add(Pet("dog", "e"))

    pet_node = cgq.poll_dog()
    print("dog", pet_node.pet.name, pet_node.pet.type)
    pet_node = cgq.poll_dog()
    print("dog", pet_node.pet.name, pet_node.pet.type)

    pet_node = cgq.poll_cat()
    print("cat", pet_node.pet.name, pet_node.pet.type)
    pet_node = cgq.poll_cat()
    print("cat", pet_node.pet.name, pet_node.pet.type)

    pet_node = cgq.poll_all()
    print("all", pet_node.pet.name, pet_node.pet.type)
    pet_node = cgq.poll_all()
    print("all", pet_node.pet.name, pet_node.pet.type)
