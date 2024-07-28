module nbits_adder #(
    parameter WIDTH = 8
) (
    input logic carry_in
    input logic [WIDTH-1:0] a,
    input logic [WIDTH-1:0] b,
    output logic [WIDTH-1:0] sum,
    output logic carry_out
);

    always_comb begin : adder
        {carry_out, sum} = a + b + carry_in;
    end : adder

endmodule