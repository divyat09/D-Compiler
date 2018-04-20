.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
as1: .long 0
Box.foo.ret: .long 0
tmp1s1: .long 0
bs0: .long 0
Box.foo_1: .long 0
hs0: .long 0
Box.foo_2: .long 0
As2.h: .long 0
As2.b: .long 0

.text
.globl _start
_start:

// Saving Context at the end of Basic Block

// Finished Saving Context at the end of Basic Block

.type Box.foo , @function
Box.foo:
push	%ebp
mov	%esp,	%ebp
movl	Box.foo_1,	%ebx
movl	%ebx,	%eax
movl	Box.foo_2,	%edx
movl	%edx,	%ecx
movl	%ebx,	Box.foo_1
movl	%eax,	%ebx
imul	%ecx,	%ebx
movl	%edx,	Box.foo_2
movl	%ebx,	%edx
movl	%ebx,	tmp1s1
movl	%eax,	%ebx
movl	%ebx,	Box.foo_1
movl	%ecx,	%ebx
movl	%ecx,	bs0
movl	%edx,	%ecx
mov	%ebp,	%esp
pop	%ebp
movl	%edx,%eax
ret
main:
movl	%edx,	as1
movl	$2,	%edx
movl	%ecx,	Box.foo.ret
movl	$19,	%ecx
movl	%eax,	hs0
movl	%edx,	%eax
movl	%ecx,	%ebx
movl	%eax,	Box.foo_1
movl	%ecx,	As2.b
movl	%edx,	As2.h
call	Box.foo
movl	Box.foo_1,	%eax
movl	%eax,	%edx
movl	%ebx,	%ecx
movl	$1,%ebx
movl	$1,%eax
int	$0x80

// Saving Context at the end of Basic Block
movl	%ebx,	Box.foo_2
movl	%eax,	Box.foo_1
movl	%edx,	As2.h
movl	%ecx,	As2.b

// Finished Saving Context at the end of Basic Block

// The End
