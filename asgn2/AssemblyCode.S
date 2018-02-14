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
movl	e,	%edx
pushl	%edx
pushl	$format_out
call	printf
addl	$8,%esp
movl	a,	%ecx
movl	%ecx,%eax
notl	%eax
movl	%eax,	j
movl	%ecx,	a
movl	j,	%edx
pushl	%edx
pushl	$format_out
call	printf
addl	$8,%esp
movl	a,	%eax
movl	%eax,	%ecx
shrl	$2,	%ecx
movl	%eax,	a
movl	%ecx,	g
movl	g,	%edx
pushl	%edx
pushl	$format_out
call	printf
addl	$8,%esp
movl	a,	%eax
movl	%eax,	%ecx
shll	$2,	%ecx
movl	%eax,	a
movl	%ecx,	h
movl	h,	%edx
pushl	%edx
pushl	$format_out
call	printf
addl	$8,%esp
movl	$0,%ebx
movl	$1,%eax
int	$0x80
