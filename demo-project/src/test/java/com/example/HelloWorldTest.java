package com.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class HelloWorldTest {

    @Test
    void testMain() {
        // Just verify no exception
        HelloWorld.main(new String[]{});
        assertTrue(true);
    }
}