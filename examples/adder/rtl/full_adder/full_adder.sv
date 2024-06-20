/*
                                half_adder_sum
                                    +-----+
carry_in--------------------------->|a   s|------------------------> sum
             +-----+                |     |             +----+
       a---->|a   s|---sum_inputs-->|b   c|--carry_sum->|    |-----> carry_out
             |     |                +-----+             | OR |
       b---->|b   c|---carry_inputs- ------------------>|    |
             +-----+                                    +----+
       half_adder_inputs
*/



module full_adder (
    input logic a,
    input logic b,
    input logic carry_in,
    output logic sum,
    output logic carry_out
);

logic sum_inputs;
logic carry_inputs;
logic carry_sum;

half_adder half_adder_inputs
(
    .a,
    .b,
    .sum(sum_inputs),
    .carry(carry_inputs)
);

half_adder half_adder_sum
(
    .a(carry_in),
    .b(sum_inputs),
    .carry(carry_sum),
    .sum
);

assign carry_out = carry_inputs | carry_sum;

endmodule