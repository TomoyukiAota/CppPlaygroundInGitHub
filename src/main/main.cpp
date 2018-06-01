#include "Hello.h"
#include <iostream>
#include <vector>
#include <numeric>
#include <memory>

struct Target
{
    int m_member = 0;

    explicit Target(const int member)
        : m_member{member}
    {
    }
};

class NotOwningClass
{
public:
    explicit NotOwningClass(Target* target) 
        : m_pTarget{target}{};

    void print() const
    {
        std::cout << m_pTarget->m_member << std::endl;;
    }


    // Default operators
    NotOwningClass(const NotOwningClass& other) = delete;

    NotOwningClass(NotOwningClass&& other) noexcept: m_pTarget{ other.m_pTarget }
    {
        other.m_pTarget = nullptr;
    };
    
    NotOwningClass& operator=(const NotOwningClass& other) = delete;

    NotOwningClass& operator=(NotOwningClass&& other) noexcept = delete;
    //{
    //    if (this != &other)
    //    {
    //        delete m_pTarget;                 // delete should not be called.
    //        m_pTarget = other.m_pTarget;
    //    }

    //    return *this;
    //};

    ~NotOwningClass() = default;;

private:
    Target* m_pTarget;
};

void printAsFreeFunc(Target* target)
{
    std::cout << target->m_member << std::endl;;
}

int main()
{
    // Use NotOwningTarget.print()
    auto target = std::make_unique<Target>(10);
    const auto targetPtr = target.get();
    NotOwningClass notOwning1{ targetPtr };
    notOwning1.print();

    NotOwningClass notOwning2{ std::move(notOwning1) };
    notOwning2.print();


    // printAsFreeFunc(Target*) to do the same
    printAsFreeFunc(targetPtr);
}

