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
h: .long 0

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
pushl	%ecx
pushl	$format_out
call	printf
addl	$8,%esp
movl	a,	%edx
movl	%edx,%eax
notl	%eax
movl	%eax,	f
movl	%ebx,	c
movl	f,	%ebx
pushl	%ebx
pushl	$format_out
call	printf
addl	$8,%esp
pushl	%edx
pushl	$format_out
call	printf
addl	$8,%esp
movl	%edx,	%eax
shrl	$2,	%eax
movl	%eax,	g
movl	%edi,	b
movl	g,	%edi
pushl	%edi
pushl	$format_out
call	printf
addl	$8,%esp
movl	%edx,	%eax
shll	$2,	%eax
movl	%eax,	h
movl	%edx,	a
movl	h,	%edx
pushl	%edx
pushl	$format_out
call	printf
addl	$8,%esp
movl	$0,%ebx
movl	$1,%eax
int	$0x80
movl	%edi,	g
movl	%ebx,	f
movl	%esi,	d
movl	%ecx,	e
movl	%edx,	h
