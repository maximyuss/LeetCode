// https://leetcode.com/problems/my-calendar-i/
class MyCalendar {
private:
	const int _MAX_VALUE_ = 1e9 + 1;
	set<pair<int, int>> store;

public:
	MyCalendar() {
		store.insert({ -1,-1 });
		store.insert({ _MAX_VALUE_,_MAX_VALUE_ });
	}

	bool book(int start, int end) {
		const pair<int, int> event{ start, end };
		const auto nextEvent = store.lower_bound(event);
		if (nextEvent->first < end)
			return false;
		const auto prevEvent = prev(nextEvent);
		if (prevEvent->second > start)
			return false;
		store.insert(event);
		return true;
	}
};
