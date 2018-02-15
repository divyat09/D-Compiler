.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
a: .long 0
b: .long 0

.text
.globl _start
_start:
movl	$7,	%eax
movl	$5,	%edi
movl	%eax,	a
movl	a,	%ebx
pushl	%ebx
pushl	$format_out
call	printf
addl	$8,%esp
pushl	%edi
pushl	$format_out
call	printf
addl	$8,%esp
movl	%edi,	b
movl	%ebx,	a
movl	a,	%eax
movl	b,	%edi
cmpl	%edi,%eax
jg	L8
movl	%eax,	a
pushl	$0
pushl	$format_out
call	printf
addl	$8,%esp
JMP	L21
movl	%edi,	b
L8:
pushl	$1
pushl	$format_out
call	printf
addl	$8,%esp
movl	a,	%eax
movl	b,	%edi
cmpl	%edi,%eax
jl	L21
movl	%eax,	a
pushl	$0
pushl	$format_out
call	printf
addl	$8,%esp
movl	%edi,	b
movl	a,	%eax
cmpl	$10,%eax
jge	L21
movl	%eax,	a
pushl	$0
pushl	$format_out
call	printf
addl	$8,%esp
movl	$7,	%eax
movl	b,	%eax
cmpl	%eax,%eax
jle	L21
movl	%eax,	b
pushl	$0
pushl	$format_out
call	printf
addl	$8,%esp
movl	$1,	%eax
cmpl	$-1,%eax
je	L21
pushl	$0
pushl	$format_out
call	printf
addl	$8,%esp
movl	b,	%eax
cmpl	$5,%eax
jne	L21
movl	%eax,	b
pushl	$0
pushl	$format_out
call	printf
addl	$8,%esp
movl	$0,%ebx
movl	$1,%eax
int	$0x80
L21:
movl	$0,%ebx
movl	$1,%eax
int	$0x80
