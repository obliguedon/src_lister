module nbits_adder #(
    parameter WIDTH = 8
) (
    input logic [WIDTH-1:0] a,
    input logic [WIDTH-1:0] b,
    output logic [WIDTH-1:0] sum,
    output logic carry
);
    logic middle_carry[WIDTH+1];

    assign middle_carry[0] = 0;
    assign carry = middle_carry[WIDTH+1];

    generate
        genvar bit_nb;
        for (bit_nb = 0; bit_nb < WIDTH; bit_nb++) begin
            full_adder u_full_adder
            (
                .a(a[bit_nb]),
                .b(b[bit_nb]),
                .carry_in(middle_carry[bit_nb]),
                .sum(sum[bit_nb]),
                .carry_out(middle_carry[bit_nb+1])
            );
        end
    endgenerate

endmodule