class Node
  attr_accessor :data, :next

  def initialize(initdata)
    @data = initdata
    @next = nil
  end
end

class UnorderedList
  def initialize
    @head = nil
  end

  def add(item)
    temp = Node.new(item)
    temp.next = @head
    @head = temp
  end

  def is_empty
    @head == nil
  end

  def size
    current = @head
    count = 0

    while !current.nil?
      count += 1
      current = current.next
    end

    return count
  end

  def search(item)
    current = @head
    found = false

    while !current.nil? and !found
      if current.data == item
        found = true
      else
        current = current.next
      end
    end

    return found
  end

  def remove(item)
    current = @head
    previous = nil
    found = false

    while !found
      if current.data == item
        found = true
      else
        previous = current
        current = current.next
    end

    if previous.nil?
      @head = current.next
    else
      previous.next = current.next
    end
  end
end
