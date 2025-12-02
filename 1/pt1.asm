.global _start
.text
_start:

  movq $0, %r8              ;# ans
  movq $50, %r9             ;# dial
  leaq input, %r10          ;# input_ptr

;# For each line of input
loop:
  cmp $end_input, %r10
  jge print_ans
  movb (%r10), %r11b        ;# first_char
  inc %r10                  ;# input_ptr++
  movq $0, %rax             ;# val

  ;# Read int value after char
loop_int_val:
  movb (%r10), %r13b        ;# *input_ptr
  cmp $0x0A, %r13           ;# '\n'
  je break_loop_int_val
  subq $0x30, %r13          ;# '0'
  imulq $10, %rax           ;# val *= 10
  addq %r13, %rax           ;# val += int(*input_ptr)   
  movq %rax, %r12
  inc %r10                  ;# input_ptr++
  jmp loop_int_val
break_loop_int_val:
  inc %r10                  ;# input_ptr++
  xorq %rdx, %rdx           ;# rdx = 0

  ;# val %= 100
  movq $100, %rcx
  divq %rcx
  movq %rdx, %r12
  xorq %rdx, %rdx           ;# rdx = 0

  ;# if char == 'L'
  cmp $0x4C, %r11           ;# 'L'
  je turn_left
turn_right:
  movq %r9, %rax            ;# temp = dial
  addq %r12, %rax           ;# temp += val
  movq $100, %rcx           ;# d = 100
  divq %rcx                 ;# q, r = temp / d
  movq %rdx, %r9            ;# dial = r
  jmp check_zero
turn_left:
  movq %r9, %rax            ;# temp = dial
  addq $100, %rax           ;# temp += 100
  subq %r12, %rax           ;# temp -= val
  movq $100, %rcx           ;# d = 100
  divq %rcx                 ;# q, r = temp / d
  movq %rdx, %r9            ;# dial = temp

check_zero:
  ;# if dial == 0
  cmp $0x0, %r9           
  jne loop
  inc %r8                   ;# ans++
  jmp loop
  
print_ans:
  
  ;# to_string()
  leaq end_ans_string, %r10
  dec %r10
  movb $0x0A, (%r10)
  movq %r8, %rax
  movq $10, %rcx
to_str_loop:
  dec %r10
  xorq %rdx, %rdx
  divq %rcx
  addq $0x30, %rdx
  movb %dl, (%r10)
  cmp $0x0, %rax
  jne to_str_loop

  ;# sys_write
  movq $1, %rax
  movq $1, %rdi
  leaq ans_string, %rsi
  movq $8, %rdx
  syscall

  ;# sys_exit
  movq $60, %rax
  xorq %rdi, %rdi
  syscall

.data
ans_string: .ascii "        "
end_ans_string:
input:
        .ascii  "INPUT_GOES_HERE"
end_input:
