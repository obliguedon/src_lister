import calculator_pkg::*;

module top #(
    parameter int BIT_WIDTH = 8
) (
    input logic                          clk,
    input logic                          reset_n,
    input logic          [BIT_WIDTH-1:0] a,
    input logic          [BIT_WIDTH-1:0] b,
    input te_operation                   operation,
    output logic         [BIT_WIDTH-1:0] result,
    output te_out_status                 status
);

logic [BIT_WIDTH-1:0] middle_a;
logic [BIT_WIDTH-1:0] middle_b;
logic [BIT_WIDTH-1:0] middle_result;

logic middle_carry_in;
logic middle_carry_out;

te_out_status middle_status;

always_comb begin : comb_add_sub
    if (operation == ADD) begin
        middle_a        = a;
        middle_b        = b;
        middle_carry_in = 0;

        if (middle_carry_out == 1) begin
            middle_status = OVERFLOW;
        end
        else begin
            middle_status = VALID;
        end
    end
    else if (operation == SUB) begin
        middle_a        = a;
        middle_b        = ~b;
        middle_carry_in = 1;
        if (middle_carry_out == 1) begin
            middle_status = NEGATIVE;
        end
        else begin
            middle_status = VALID;
        end
    end
end : comb_add_sub

always_ff @( posedge clk or negedge reset_n ) begin : seq_assign_output
    if (reset_n == 0) begin
        result <= 0;
        status <= STANDBY;
    end
    else begin
        result <= middle_result;
        status <= middle_status;
    end
end : seq_assign_output

nbits_adder #(
    .WIDTH(BIT_WIDTH)
) inst_adder (
    .carry_in (middle_carry_in ),
    .a        (middle_a        ),
    .b        (middle_b        ),
    .sum      (middle_result   ),
    .carry_out(middle_carry_out)
);

endmodule