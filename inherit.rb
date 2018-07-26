class P
  def foo
    p "P"
  end

end

class B
  def foo
    p "B"
  end
end

a = B.new
a.foo
