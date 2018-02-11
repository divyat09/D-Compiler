.data
a: .long 0
c: .long 0
b: .long 0
format_string: .asciz "%d\n"
.text
.global _start
_start:
movl	$5,	%eax
movl	$3,	%edi
movl	%eax,	%ebx
addl	%edi,	%ebx
movl	%ebx,	c
movl	%eax,	a
//movl	$5,	%edx
//movl	$c,	%ecx
//movl	$4,	%eax
//movl	$1,	%ebx
//int	$0x80
pushl   %ebx
pushl   $format_string
call    printf

movl    $1,%eax
int $0x80
