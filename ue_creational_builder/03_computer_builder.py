# Develop a ComputerBuilder that allows users to select components like CPU, GPU, RAM, and storage.
# This builder should validate combinations to ensure compatibility.



if __name__ == '__main__':
    computer_builder = ComputerBuilder()
    computer = computer_builder.set_cpu("Intel i7")\
                               .set_gpu("NVIDIA RTX 3080")\
                               .add_ram("16GB DDR4")\
                               .add_storage("1TB SSD")\
                               .build()
    print(computer)
