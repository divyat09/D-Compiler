.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
main.ret: .long 0
tmp2s1: .long 0
is0: .long 0
tmp1s0: .long 0

.text
.globl _start

// Saving Context at the end of Basic Block

// Finished Saving Context at the end of Basic Block
_start:
main:
movl	$0,	%ebx
L1:
cmpl	$10,%ebx
jl	LL1
movl	$0,	%eax
JMP	LL0
LL1:
movl	$1,	%eax
LL0:

// Saving Context at the end of Basic Block
movl	%ebx,	is0
movl	%eax,	tmp1s0

// Finished Saving Context at the end of Basic Block
movl	tmp1s0,	%ebx
cmpl	$0,%ebx
je	L2
movl	is0,	%eax
movl	%eax,	%edx
addl	$1,	%edx
movl	%edx,	%eax

// Saving Context at the end of Basic Block
movl	%ebx,	tmp1s0
movl	%eax,	is0
movl	%edx,	tmp2s1

// Finished Saving Context at the end of Basic Block
JMP	L1

// Saving Context at the end of Basic Block

// Finished Saving Context at the end of Basic Block
L2:
movl	$1,	%ebx
movl	$1,%ebx
movl	$1,%eax
int	$0x80

// Saving Context at the end of Basic Block
movl	%ebx,	main.ret

// Finished Saving Context at the end of Basic Block

// The End
