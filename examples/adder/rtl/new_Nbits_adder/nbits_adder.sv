module nbits_adder #(
    parameter WIDTH = 8
) (
    input logic [WIDTH-1:0] a,
    input logic [WIDTH-1:0] b,
    output logic [WIDTH-1:0] sum,
    output logic carry
);

    always_comb begin : adder
        {carry, sum} = a + b;
    end : adder
    
endmodule