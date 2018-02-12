.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
i: .long 0
A: .zero 40

.text
.globl _start
_start:
movl	$0,	%eax
L2:
movl	%eax,	i
movl	i,	%ebx
movl	$4,	%esi
xorl	%eax,%eax
movl	$A,	%edi
imul	%ebx,	%esi
addl	%esi,	%edi
pushl	%edi
pushl	$format_in
call	scanf
addl	$8,%esp
addl	$1,	%ebx
movl	%edi,	A
movl	%ebx,	i
movl	i,	%eax
cmpl	$10,%eax
jl	L2
movl	$0,	%eax
L7:
movl	%eax,	i
movl	$A,	%edi
movl	i,	%ebx
movl	(%edi, %ebx, 4),	%esi
pushl	%esi
pushl	$format_out
call	printf
addl	$8,%esp
addl	$1,	%ebx
movl	%edi,	A
movl	%ebx,	i
movl	i,	%eax
cmpl	$10,%eax
jl	L7
movl	%eax,	i
movl	$A,	%edi
movl	$5,	%ebx
movl	(%edi, %ebx, 4),	%ebx
pushl	%ebx
pushl	$format_out
call	printf
addl	$8,%esp
movl	$A,	%edi
movl	$7,	%ecx
movl	(%edi, %ecx, 4),	%ecx
pushl	%ecx
pushl	$format_out
call	printf
addl	$8,%esp
movl	$0,%ebx
movl	$1,%eax
int	$0x80
movl	%edi,	A
