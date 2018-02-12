.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
a: .long 0

.text
.globl _start
_start:
movl	$0,	%eax
movl	%eax,	a
xorl	%eax,%eax
pushl	$a
pushl	$format_in
call	scanf
addl	$8,%esp
pushl	a
pushl	$format_out
call	printf
addl	$8,%esp
movl	$0,%ebx
movl	$1,%eax
int	$0x80
