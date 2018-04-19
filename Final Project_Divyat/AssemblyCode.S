.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
i: .long 0
A: .zero 40
j: .long 0

.text
.globl _start
_start:
movl	$0,	%ebx

// Saving Context at the end of Basic Block
movl	%ebx,	i
L2:
movl	i,	%edx
movl	$4,	%ecx
xorl	%eax,%eax
movl	$A,	%ebx
imul	%edx,	%ecx
addl	%ecx,	%ebx
pushl	%ebx
pushl	$format_in
call	scanf
addl	$8,%esp
addl	$1,	%edx

// Saving Context at the end of Basic Block
movl	%ebx,	A
movl	%edx,	i
movl	i,	%ebx
cmpl	$10,%ebx
jl	L2
movl	$0,	%ebx

// Saving Context at the end of Basic Block
movl	%ebx,	i
L7:
movl	i,	%ebx
movl	$9,	%eax
subl	%ebx,	%eax
movl	%eax,	j
movl	%ebx,	i
movl	$A,	%esi
movl	j,	%edi
movl	(%esi, %edi, 4),	%ebx
pushl	%ebx
pushl	$format_out
call	printf
addl	$8,%esp
// Noooooo
// Noooooo
// Noooooo
// Noooooo
movl	i,	%eax
addl	$1,	%eax
movl	%eax,	i
movl	$A,	%esi
movl	$j,	%edi
movl	%ebx,	(%esi, %edi, 4)
movl	i,	%ebx
pushl	%ebx
pushl	$format_out
call	printf
addl	$8,%esp
// Noooooo
// Noooooo
// Noooooo
// Noooooo

// Saving Context at the end of Basic Block
movl	%ebx,	i
movl	i,	%ebx
cmpl	$10,%ebx
jl	L7
movl	$1,%ebx
movl	$1,%eax
int	$0x80
