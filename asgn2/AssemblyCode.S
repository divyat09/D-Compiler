.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
a: .long 0
c: .long 0
b: .long 0
e: .long 0
d: .long 0
g: .long 0
h: .long 0
j: .long 0

.text
.globl _start
_start:
movl	$10,	%eax
movl	$5,	%edi
movl	%eax,	%ebx
orl	%edi,	%ebx
movl	%eax,	a
pushl	%ebx
pushl	$format_out
call	printf
addl	$8,%esp
movl	a,	%eax
movl	%eax,	%esi
andl	%edi,	%esi
movl	%eax,	a
pushl	%esi
pushl	$format_out
call	printf
addl	$8,%esp
movl	a,	%eax
movl	%eax,	%ecx
xorl	%edi,	%ecx
movl	%eax,	a
movl	%ecx,	e
movl	%ebx,	c
movl	e,	%ebx
pushl	%ebx
pushl	$format_out
call	printf
addl	$8,%esp
movl	a,	%ecx
movl	%ecx,%eax
notl	%eax
movl	%eax,	j
movl	%ecx,	a
movl	%edi,	b
movl	j,	%edi
pushl	%edi
pushl	$format_out
call	printf
addl	$8,%esp
movl	%edi,%edi
notl	%edi
pushl	%edi
pushl	$format_out
call	printf
addl	$8,%esp
movl	$-12,	%eax
movl	%eax,%edi
notl	%edi
pushl	%edi
pushl	$format_out
call	printf
addl	$8,%esp
movl	a,	%edx
movl	%edx,	%eax
shrl	$2,	%eax
movl	%eax,	g
movl	%edx,	a
movl	%ebx,	e
movl	g,	%ebx
pushl	%ebx
pushl	$format_out
call	printf
addl	$8,%esp
movl	a,	%edx
movl	%edx,	%eax
shll	$2,	%eax
movl	%eax,	h
movl	%edx,	a
movl	%esi,	d
movl	h,	%esi
pushl	%esi
pushl	$format_out
call	printf
addl	$8,%esp
movl	%ebx,%ecx
movl	$1,	%eax
shrl	%cl,	%eax
movl	%eax,	%ebx
pushl	%ebx
pushl	$format_out
call	printf
addl	$8,%esp
movl	$1,	%esi
shll	$5,	%esi
pushl	%esi
pushl	$format_out
call	printf
addl	$8,%esp
movl	$0,%ebx
movl	$1,%eax
int	$0x80
