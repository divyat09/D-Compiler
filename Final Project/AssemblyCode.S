.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
A: .zero 40
tmp1: .long 0
tmp3: .long 0
tmp2: .long 0

.text
.globl _start
_start:

// Saving Context at the end of Basic Block
main:
movl	$A,	%eax
movl	$2,	%edi
movl	(%eax, %edi, 4),	%edi
movl	$3,	%edi
movl	$A,	%eax
movl	$1,	%ebx
movl	(%eax, %ebx, 4),	%ebx
movl	$2,	%ebx
movl	$A,	%eax
movl	$0,	%esi
movl	(%eax, %esi, 4),	%esi
movl	$1,	%esi
movl	%esi,	%ecx
imul	%ebx,	%ecx
movl	%ecx,	%edi
movl	%eax,	A
movl	%esi,	%eax
cdq
idiv	%edi
movl	tmp2,	%edx
movl	%eax,	%edx
movl	%edx,	%ebx
movl	%ebx,	%eax
addl	%edi,	%eax
movl	%eax,	%esi

// Saving Context at the end of Basic Block
movl	%eax,	tmp3
movl	$A,	%eax
movl	%ebx,	A[1]
movl	$2,	%ebx
movl	%edi,	(%eax, %ebx, 4)
movl	A[1],	%ebx
movl	$A,	%eax
movl	$1,	%edi
movl	%ebx,	(%eax, %edi, 4)
movl	$A,	%eax
movl	$0,	%edi
movl	%esi,	(%eax, %edi, 4)
movl	%ecx,	tmp1
movl	%edx,	tmp2
