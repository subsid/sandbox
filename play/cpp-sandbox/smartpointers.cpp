// Thanks Cherno! https://www.youtube.com/watch?v=UOB7-B2MfwA
#include<iostream>
#include<string>
#include<memory>

class Entity {
  public:
    Entity() {
      std::cout << "Created Entity" << std::endl;
    }

    ~Entity() {
      std::cout << "Destroyed Entity" << std::endl;
    }
};

class ScopedPtr {
  private:
    Entity* ptr;

  public:
    ScopedPtr(Entity *_ptr) : ptr(_ptr) {
    }

    ~ScopedPtr() {
      std::cout << "Scope destructor" << std::endl;
      delete ptr;
    }
};

int main() {
  /* { */
  /*   // Raw pointer, does not delete object from heap at end of scope. */
  /*   Entity* e = new Entity(); */
  /* } */

  /* { */
  /*   // Manual smart pointer */
  /*   ScopedPtr e(new Entity()); */
  /* } */

  /* { */
  /*   // Unique smart pointer */
  /*   std::unique_ptr<Entity> entity(new Entity()); */

  /*   // Not possible, they are unique! */
  /*   /1* std::unique_ptr<Entity> e0 = entity; *1/ */
  /* } */

  /* { */
  /*   // Shared pointers can be used to assign pointers to multiple vars. */
  /*   std::shared_ptr<Entity> e0; */
  /*   { */

  /*     // Good idea to use make_shared (vs just creating the object), so that the reference counting and the pointer box is put in the same object. */
  /*     std::shared_ptr<Entity> e1 = std::make_shared<Entity>(); */
  /*     e0 = e1; */
  /*     std::cout << "End of inner scope" << std::endl; */
  /*   } */

  /*     std::cout << "End of outer scope" << std::endl; */
  /* } */

  /* { */
  /*   // Shared weak ptr, does not add to the reference count. */
  /*   std::weak_ptr<Entity> e0; */
  /*   { */

  /*     // Good idea to use make_shared (vs just creating the object), so that the reference counting and the pointer box is put in the same object. */
  /*     std::shared_ptr<Entity> e1 = std::make_shared<Entity>(); */
  /*     e0 = e1; */
  /*     std::cout << "End of inner scope" << std::endl; */
  /*   } */

  /*     std::cout << "End of outer scope" << std::endl; */
  /* } */

  std::cout << "Done" << std::endl;;

  return 0;
}
