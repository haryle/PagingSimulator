from mmu import MMU


class RandMMU(MMU):
    def __init__(self, frames):
        # TODO: Constructor logic for RandMMU
        super().__init__()
        self.frames = frames

    def read_memory(self, page_number):
        # TODO: Implement the method to read memory
        pass

    def write_memory(self, page_number):
        # TODO: Implement the method to write memory
        pass