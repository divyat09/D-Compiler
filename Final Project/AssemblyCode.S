.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
main.ret: .long 0
as0: .long 0
bs0: .long 0
tmp1s0: .long 0

.text
.globl _start
_start:

// Saving Context at the end of Basic Block

// Finished Saving Context at the end of Basic Block
main:
movl	$1,	%ebx
movl	$2,	%eax
movl	%ebx,	%edx
addl	%eax,	%edx
movl	%edx,	%ebx
movl	%eax,	bs0
movl	%edx,	tmp1s0
movl	%ebx,	as0
movl	bs0,	%ebx
pushl	%ebx
pushl	$format_out
call	printf
addl	$8,%esp
movl	%ebx,	bs0
movl	as0,	%ebx
pushl	%ebx
pushl	$format_out
call	printf
addl	$8,%esp
movl	$0,	%eax
movl	$0,%ebx
movl	$1,%eax
int	$0x80

// Saving Context at the end of Basic Block
movl	%ebx,	as0
movl	%eax,	main.ret

// Finished Saving Context at the end of Basic Block

// The End
