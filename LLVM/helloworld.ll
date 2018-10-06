; Need C standard library
declare i32 @puts(i8* nocapture) nounwind

define i32 @main() {
  %s = alloca i128
  %1 = mul i128 13122668973721, 1156440705169
  %2 = mul i128 %1, 8
  store i128 %2, i128* %s
  %cst = bitcast i128* %s to i8*
  call i32 @puts(i8* %cst)
  ret i32 0
}
