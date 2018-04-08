.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
a: .long 0

.text
.globl _start
_start:
movl	$5,	%eax
movl	%eax,	a
movl	a,	%eax
cmpl	$5,%eax
je	L1
movl	$1,	%eax
movl	%eax,	a
movl	a,	%edi
pushl	%edi
pushl	$format_out
call	printf
addl	$8,%esp
movl	$0,%ebx
movl	$1,%eax
int	$0x80
L1:
movl	$2,	%edi
pushl	%edi
pushl	$format_out
call	printf
addl	$8,%esp
movl	$0,%ebx
movl	$1,%eax
int	$0x80
