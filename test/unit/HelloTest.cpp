#include "Hello.h"
#include "gmock/gmock.h"
#include <gsl/gsl>

using namespace ::testing;

TEST(Hello, getHelloWorld_ReturnsHelloWorld)
{
    const auto expected = "Hello World!";
    const auto actual = getHelloWorld();
    ASSERT_THAT(actual, Eq(expected));
}

TEST(gsl, experiment)
{
    const std::vector<int> vec{ 10, 20, 30 };
    const gsl::span<const int> s{ vec };

    ASSERT_THAT(s[0], Eq(vec[0]));
    ASSERT_THAT(s[1], Eq(vec[1]));
    ASSERT_THAT(s[2], Eq(vec[2]));
}