.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
A: .zero 40
tmp1: .long 0

.text
.globl _start
_start:

// Saving Context at the end of Basic Block
main:
// B 2 Assign 
// B Base Assign
// E Base Assign 
movl	$A,	%eax
movl	$2,	%edi
movl	(%eax, %edi, 4),	%edi
// E 2 Assign 
movl	$3,	%edi
// B 2 Assign 
// B Base Assign
// E Base Assign 
movl	$A,	%eax
movl	$1,	%ebx
movl	(%eax, %ebx, 4),	%ebx
// E 2 Assign 
movl	$2,	%ebx
// B 2 Assign 
// B Base Assign
// E Base Assign 
movl	$A,	%eax
movl	$0,	%esi
movl	(%eax, %esi, 4),	%esi
// E 2 Assign 
movl	$1,	%esi
// B 1 Operator 1 Assign
// E 1 Operator 1 Assign
// B 2 Operator 1 Assign
// E 2 Operator 1 Assign
// B 3 Operator 1 Assign
// E 3 Operator 1 Assign
movl	%esi,	%ecx
addl	%ebx,	%ecx
// B 1 Assign 
// E 1 Assign 
// B 2 Assign 
// E 2 Assign 
movl	%ecx,	%edi
// Here %eax
// %eax	A
movl	%eax,	A
// %eax	AFreed
// DONE %eax
// Here %ecx
// %ecx	tmp1
movl	%ecx,	tmp1
// %ecx	tmp1Freed
// DONE %ecx
//2
//	HELLLL
// B 1 Print 
// B V Assign Spill FORtmp1
//B_Spilling
// %esi	A[0]
// %esi	A[0]
movl	%eax,	None
movl	$A,	%eax
movl	%edi,	A[2]
movl	$0,	%edi
movl	%esi,	(%eax, %edi, 4)
movl	None,	%eax
movl	A[2],	%edi
// %esi	A[0]Freed
//E_Spilling
// E V Assign Spill FORtmp1
movl	tmp1,	%esi
// E 1 Print 
pushl	%esi
pushl	$format_out
call	printf
addl	$8,%esp
movl	$1,%ebx
movl	$1,%eax
int	$0x80

// Saving Context at the end of Basic Block
// %edi	A[2]
// %edi	A[2]
movl	$A,	%eax
movl	$2,	%ecx
movl	%edi,	(%eax, %ecx, 4)
// %edi	A[2]Freed
// %ebx	A[1]
// %ebx	A[1]
movl	$A,	%eax
movl	$1,	%edi
movl	%ebx,	(%eax, %edi, 4)
// %ebx	A[1]Freed
// %esi	tmp1
movl	%esi,	tmp1
// %esi	tmp1Freed
