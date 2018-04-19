#include "Hello.h"
#include "gmock/gmock.h"

using namespace ::testing;

TEST(Hello, getHelloWorld_ReturnsHelloWorld)
{
    const auto expected = "Hello World!";
    const auto actual = getHelloWorld();
    ASSERT_THAT(actual, Eq(expected));
}