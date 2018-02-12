.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
a: .long 0
c: .long 0
b: .long 0
e: .long 0
d: .long 0
g: .long 0
f: .long 0
i: .long 0
h: .long 0
j: .long 0

.text
.globl _start
_start:
movl	$10,	%eax
movl	$5,	%edi
movl	%eax,	%ebx
addl	%edi,	%ebx
movl	%ebx,	c
movl	%ebx,	c
pushl	c
pushl	$format_out
call	printf
addl	$8,%esp
movl	%eax,	%ebx
subl	%edi,	%ebx
movl	%ebx,	d
movl	%ebx,	d
pushl	d
pushl	$format_out
call	printf
addl	$8,%esp
movl	%eax,	%ebx
imul	%edi,	%ebx
movl	%ebx,	e
movl	%ebx,	e
pushl	e
pushl	$format_out
call	printf
addl	$8,%esp
movl	%eax,	a
movl	a,	%ebx
movl	%ebx,	%eax
cdq
idiv	%edi
movl	%eax,	f
movl	%eax,	f
pushl	f
pushl	$format_out
call	printf
addl	$8,%esp
pushl	g
pushl	$format_out
call	printf
addl	$8,%esp
pushl	h
pushl	$format_out
call	printf
addl	$8,%esp
pushl	i
pushl	$format_out
call	printf
addl	$8,%esp
not	%eax,%ebx
movl	%eax,	j
movl	%eax,	j
pushl	j
pushl	$format_out
call	printf
addl	$8,%esp
movl	$0,%ebx
movl	$1,%eax
int	$0x80
movl	%edi,	b
movl	%ebx,	a
