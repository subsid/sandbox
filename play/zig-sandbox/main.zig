const std = @import("std");
const expect = @import("std").testing.expect;

pub fn main() void {
    // Variables
    const a: u8 = 0;
    var b: u8 = 5;
    b = 10;

    // Constants
    const c: u8 = 5;

    // Type coercion
    const d: u8 = @as(u8, 5);

    // Undefined but needs a type
    const e: u32 = undefined;

    std.debug.print("{d}, {d}, {d}, {d}, {d}!\n", .{ a, b, c, d, e });

    // Arrays
    const arr = [3]u8{ 1, 2, 3 };

    std.debug.print("{d}, {d}, {d} Length: {d}!\n", .{ arr[0], arr[1], arr[2], arr.len });
}

test "zig has inbuilt testing!!" {
    const b = 10;
    // If can be statements and expressions.
    const a = if (b == 10) true else false;
    var x: u32 = 5;

    if (a) {
        x += 5;
    } else {
        x += 10;
    }

    try expect(x == 10);
}

test "defer" {
    // Executed before a block exits
    // Executes in reverse order. Think of a stack.
    var x: u8 = 5;

    {
        defer x += 2;
        // Print without arguments
        std.debug.print("****\n", .{});
        std.debug.print("X value is {d}", .{x});
        try expect(x == 5);
    }

    try expect(x == 7);
}

test "error values and unions in zig" {}
