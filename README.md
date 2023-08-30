The program `memsim.py` processes the input and calls the mmu unit to read or write a page.
Do not modify the inpt or output of this file. You may modify the calls to mmu.

The memory management unit (mmu) should keep track of the contents of the page table in the format you see most
appropiate

Each page should have a modified bit set to 0 when loaded, and set to 1 when the access is a write

when a page is not resident you should:

- count this as a page fault (as we need to read it from disk).
- find a free frame to allocate it
- if there are no free frame, then you need to choose a victim to swap as per lru/rand/clock policy
- if the victim is modified, then you need to count a disk write.

The class mmu has a list of methods that you can use as a guide for implementing the memmory management unit.
You may change the mmu interface and/or add new methods when implementing read_memory.
Start by thinking which class attributes you need and what is their initial value.

Other notes on code development
We will run the test in quiet mode. You must use the debug attribute to print messages for debugging purposes. 



