
FLAG?=FPGA

sim:
	files_lister --top-yaml ./verif/adder_tb.yml --template ./templates/run_verilator.txt --flag $(FLAG) --output-file run_verilator.sh
	chmod +x ./run_verilator.sh
	./run_verilator.sh
	./obj_dir/dut

lint:
	files_lister --top-yaml ./rtl/Nbits_adder/nbits_adder.yml --template ./templates/lint_verilator.txt --flag $(FLAG) --output-file lint_verilator.sh
	chmod +x ./lint_verilator.sh
	./lint_verilator.sh

clean:
	rm -r ./obj_dir
	rm ./dump.vcd