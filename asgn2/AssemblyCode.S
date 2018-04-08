.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
a: .long 0
c: .long 0
b: .long 0

.text
.globl _start
_start:
xorl	%eax,%eax
pushl	$a
pushl	$format_in
call	scanf
addl	$8,%esp
xorl	%eax,%eax
pushl	$b
pushl	$format_in
call	scanf
addl	$8,%esp
xorl	%eax,%eax
pushl	$c
pushl	$format_in
call	scanf
addl	$8,%esp
movl	a,	%eax
movl	b,	%edi
cmpl	%edi,%eax
jle	L11
movl	%eax,	a
movl	%edi,	b
movl	b,	%eax
movl	c,	%edi
cmpl	%edi,%eax
jg	L8
movl	%eax,	b
movl	b,	%ebx
pushl	%ebx
pushl	$format_out
call	printf
addl	$8,%esp
movl	$0,%ebx
movl	$1,%eax
int	$0x80
movl	%edi,	c
movl	%ebx,	b
L8:
movl	c,	%edi
pushl	%edi
pushl	$format_out
call	printf
addl	$8,%esp
movl	$0,%ebx
movl	$1,%eax
int	$0x80
movl	%edi,	c
L11:
movl	a,	%eax
movl	c,	%edi
cmpl	%edi,%eax
jl	L15
movl	%eax,	a
pushl	%edi
pushl	$format_out
call	printf
addl	$8,%esp
movl	$0,%ebx
movl	$1,%eax
int	$0x80
movl	%edi,	c
L15:
movl	a,	%edi
pushl	%edi
pushl	$format_out
call	printf
addl	$8,%esp
movl	$0,%ebx
movl	$1,%eax
int	$0x80
