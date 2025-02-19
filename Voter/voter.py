# Sample election data: (Constituency, Candidate, Party, Votes)
election_data = [
    ("Bangalore South", "Rahul Sharma", "Party A", 35000),
    ("Bangalore South", "Vikram Rao", "Party B", 34000),
    ("Bangalore South", "Anil Kumar", "Party C", 5000),
    ("Mysore", "Suresh Gowda", "Party A", 25000),
    ("Mysore", "Manoj Shetty", "Party B", 27000),
    ("Mysore", "Ravi Kumar", "Party C", 10000),
    ("Mangalore", "Prakash Naik", "Party A", 30000),
    ("Mangalore", "Joseph D'Souza", "Party B", 29000),
    ("Mangalore", "Harish Bhat", "Party C", 8000)
]

# Step 1: Store party-wise total votes
party_votes = {}
constituency_results = {}

# Iterate through the election data
for constituency, candidate, party, votes in election_data:
    if party not in party_votes:
        party_votes[party] = 0
    party_votes[party] += votes

    if constituency not in constituency_results:
        constituency_results[constituency] = []
    constituency_results[constituency].append((votes, candidate, party))

# Step 2: Identify winners and close contests
winners = {}
close_contests = []

# Iterate through the constituency results
for constituency, results in constituency_results.items():
    # Sort candidates based on votes in descending order (votes are at index 0 in the tuple)
    results.sort(reverse=True, key=lambda x: x[0])
    
    # Get the winner (candidate with the highest votes)
    winner = results[0]  
    winners[constituency] = winner
    
    # Optional: Identify close contests (if needed)
    if len(results) > 1:
        margin = (winner[0] - results[1][0]) / winner[0] * 100
        if margin < 12:
            close_contests.append((constituency, margin))

# Step 3: Calculate vote share percentage for each party
total_votes = sum(party_votes.values())
vote_share = {party: (votes / total_votes) * 100 for party, votes in party_votes.items()}

# Determine overall winning party
overall_winner = max(party_votes, key=party_votes.get)

# Display results
print("Winning Candidates in Each Constituency:")
for constituency, (votes, candidate, party) in winners.items():
    print(f"{constituency}: {candidate} ({party}) - {votes} votes")

print("\nVote Share Percentage:")
for party, share in vote_share.items():
    print(f"{party}: {share:.2f}%")

print(f"\nOverall Winning Party: {overall_winner}")

print("\nClose Contests (Margin < 12%):")
for constituency, margin in close_contests:
    print(f"{constituency}: Margin {margin:.2f}%")
